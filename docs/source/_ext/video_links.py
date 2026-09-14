"""Sphinx directive for videos managed by the repository export_urls.csv."""

from __future__ import annotations

import csv
from pathlib import Path

from docutils import nodes
from docutils.parsers.rst import Directive
from sphinx.util import logging

logger = logging.getLogger(__name__)


def _load_urls(app):
    csv_path = Path(app.srcdir).parents[1] / "export_urls.csv"
    exact, by_name = {}, {}
    if not csv_path.is_file():
        logger.warning("video URL manifest not found: %s", csv_path)
        return exact, by_name
    with csv_path.open("r", encoding="utf-8-sig", newline="") as stream:
        for row in csv.DictReader(stream):
            obj = (row.get("object") or "").strip()
            url = (row.get("url") or "").strip()
            if not obj or not url:
                continue
            exact[obj] = url
            filename = Path(obj.replace("\\", "/")).name
            by_name.setdefault(filename, []).append((obj, url))
    return exact, by_name


def _resolve_video(app, key, source, line):
    exact, by_name = app._video_url_manifest
    key = key.strip()
    if key in exact:
        return exact[key]
    filename = Path(key.replace("\\", "/")).name
    matches = by_name.get(filename, [])
    if len(matches) == 1:
        return matches[0][1]
    if len(matches) > 1:
        logger.warning("ambiguous video object name %r; use its full object path", key, location=(source, line))
    else:
        logger.warning("video object not found in export_urls.csv: %r", key, location=(source, line))
    return None


class VideoDirective(Directive):
    required_arguments = 1
    optional_arguments = 0
    has_content = False
    final_argument_whitespace = True

    def run(self):
        key = self.arguments[0]
        url = _resolve_video(self.env.app, key, self.state.document.current_source, self.lineno)
        if url is None:
            return [nodes.literal_block(self.block_text, self.block_text)]

        raw = (
            '<div style="width: 100%; text-align: center;">'
            '<video width="100%" controls>'
            f'<source src="{url}" type="video/mp4">'
            '</video></div>'
        )
        return [nodes.raw('', raw, format='html')]


def setup(app):
    app._video_url_manifest = _load_urls(app)
    app.add_directive("video", VideoDirective)
    return {"version": "2.0", "parallel_read_safe": True}