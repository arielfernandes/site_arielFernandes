from flask import Blueprint, render_template, request
import markdown
import markdown.extensions.codehilite
from pygments.formatters import HtmlFormatter
import markdown.extensions.fenced_code


agenda_blueprint = Blueprint(
    'agenda', 'name', template_folder='templates', static_folder='static')


@agenda_blueprint.route('/')
def index():
    return render_template('index.html')


@agenda_blueprint.route('/timetable')
def timetable():
    return render_template('timetable.html')


@agenda_blueprint.route('/conteudos')
def conteudos():
    readme_file = open("templates/md/introCPP.md", "r")
    md_template_string = markdown.markdown(readme_file.read(),
                                           extensions=["fenced_code",
                                                       "codehilite",
                                                       "tables"])
    formatter = HtmlFormatter(style="monokai",
                              full=True, cssclass="codehilite")
    css_string = formatter.get_style_defs('.codehilite')
    md_css_string = "<style>" + css_string + "</style>"
    md_template = md_css_string + md_template_string
    return render_template('introcpp.html', md_text=md_template)


@agenda_blueprint.route("/teste")
def teste():
    readme_file = open("templates/md/introCPP.md", "r")
    md_template_string = markdown.markdown(
        readme_file.read(), extensions=["codehilite"]
    )

    # Generate Css for syntax highlighting
    formatter = HtmlFormatter(style="emacs", full=True, cssclass="codehilite")
    css_string = formatter.get_style_defs()
    md_css_string = "<style>" + css_string + "</style>"

    md_template = md_css_string + md_template_string
    return md_template
