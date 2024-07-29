from pathlib import Path

from django.urls import path
from sphinx_view import DocumentationView

urlpatterns = [
    # ...
    path(
        "docs<path:path>",
        DocumentationView.as_view(
            json_build_dir=Path('/fall_2024/json_view/json'),
            base_template_name="docs_base.html",
        ),
        name="documentation",
    ),
    # ...
]