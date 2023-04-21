from dash           import (
    html, 
)
from dash_iconify   import DashIconify
import dash_mantine_components as dmc
from ..static       import (
    maxdmg_name,
    maxdmg_description,
    maxdmg_github,
    maxdmg_demo,
    maxdmg_tech, 
    tools,
)


# forgive me Father for I have sinned

contacts_page = html.Div(html.Pre(
    id='contacts_page',
    className='code',
    children=[
        html.Code([html.Span(className='th'),html.Span(children=["from "], className="kw3 "),"dataclasses ",html.Span(children=["import "], className="kw3"),"dataclass"], className='tr'),
        html.Code([html.Span(className='th'),""], className='tr'),
        html.Code([html.Span(className='th'),""], className='tr'),
        html.Code([html.Span(className='th'),html.Span(children=["@dataclass"], className="kw1"),":"], className='tr'),
        html.Code([html.Span(className='th'),html.Span(children=["class "], className="kw2"), html.Span(children=["Contacts"], className="decl"), ":"], className='tr'),
        html.Code([html.Span(className='th'),"    email: ", html.Span(children="Link", className="kw3"), " = ", '"',html.A(children=["contact@tonotonokon.com"], href="mailto:contact@tonotonokon.com"),'"',], className='tr'),
        html.Code([html.Span(className='th'),""], className='tr'),
        html.Code([html.Span(className='th'),html.Span(children=["# Always happy to hear from you!"], className="comment"),], className='tr'),
        html.Code([html.Span(className='th'),""], className='tr'),
    ]
))

projects_page = html.Pre(
    id='projects_page',
    className='code',
    children=[
        html.Code([html.Span(children=["#include <stdlib.h> "], className="kw1"),]),
        #html.Code([html.Span(children=["#include <string> "], className="kw1"),]),
        html.Code([html.Span(children=['#include "Project.h"'], className="kw1"),]),
        html.Code(""),
        html.Code(""),
        #html.Code([html.Span(children=["namespace "], className="kw3"),"maxdmg "]),
        #html.Code(["{"]),
        #html.Code(["}"]),
        #html.Code(""),
        html.Code([html.Span(children=["int "], className="kw2"),"main() "]),
        html.Code(["{"]),
        html.Code([html.Span(children=["    Project "], className="decl"),"maxdmg {"]),
        html.Code(["        .name = ",html.Span(children=['"'+maxdmg_name+'"'], className="kw1"),",",]),
        html.Code(["        .desc = ",html.Span(children=['"'+maxdmg_description+'"'], className="kw1"),",",]),
        html.Code(["       .link = Link(",html.Span(children=['"',html.A([maxdmg_github], href=maxdmg_github),'"'], className="kw1"),"),",]),
        html.Code(["       .demo = Link(",html.Span(children=['"',html.A([maxdmg_demo], href=maxdmg_github),'"'], className="kw1"),"),",]),
        html.Code(["       .tech = {",]),
        html.Code(['            ', html.Span(children=[html.Span(children=[f'"{t}", ',], className='kw1',) for t in maxdmg_tech]),]),
        html.Code(["        },",]),
        html.Code(["    }"]),
        html.Code(""),
        html.Code([html.Span(children=["    exit"], className="kw3"),"(0);",]),
        html.Code(["}"]),
    ],
)

readme_page = html.Pre(
    id='readme_page',
    className='code',
    children=[
        html.H1([html.Span(id='hi', children=['Hi!',]), " I`m Anton🖖",],),
        html.Div([
          html.P(["My calling always was making real world ", html.Span(className='text_emp_1', children=['problems solved']),".",], className='readme_line',),
          html.P(["I've been doing it for ", html.Span(className='text_emp_2', children=['more then seven years'],), ' as a lawyer💼.'], className='readme_line',),
          html.P(['',], className='readme_line',),
          html.P(["    But one day a hurricane🌪 stole my briefcase..."], className='readme_line text_emp_3',),
          html.P(['',], className='readme_line',),
        ], className='readme_block',),
        html.Div([
          html.P(["Long story short, now I'm ", html.Span(className='text_emp_1', children=['solving problems'])," with my products.",], className='readme_line',),
        ], className='readme_block',),
        html.Div([
            html.P(["My ", html.Span(className='text_emp_2', children=['key technologies']),"🔧 are:",], className='readme_line',),
        ], className='readme_block',),
        html.Div([
          dmc.Stack([
            dmc.Paper([
                dmc.Divider(label=k, size='xs',variant="dotted",className='paper_title',), dmc.Paper([dmc.Badge([t,], className="badge",) for t in v], className="badge_container",), 
            ], className="paper_container", radius='md',) for k, v in tools.items()
          ]),
        ], className='readme_block',),
        html.Div([
            dmc.Divider(size='md', className='divider',),
        ], className='readme_block',),
        html.Div([
            html.P(['by the way, have you checked this terminal? it`s interactive!'], className='page_comment'),
        ], className='readme_block',),
    ],
)

right_tabs = html.Div(
    id='editor_area',
    children=[
        dmc.Tabs(
            id="editor_tabs",
            orientation="horizontal",
            variant="outline",
            activateTabWithKeyboard=True,
            loop=True,
            radius=0,
            children=[
                dmc.TabsList([
                    dmc.Tab("Readme.md"   , value="readme_tab",   className='font', icon=DashIconify(icon='file-icons:markdownlint'),),
                    dmc.Tab("Projects.cpp", value="projects_tab", className='font', icon=DashIconify(icon='mdi:language-cpp'),),
                    dmc.Tab("Contacts.py" , value="contacts_tab", className='font', icon=DashIconify(icon='mdi:language-python'),),
                ]),
                dmc.TabsPanel(id='read_tab', children=[readme_page,], value="readme_tab"),
                dmc.TabsPanel(id='proj_tab', children=[projects_page,], value="projects_tab"),
                dmc.TabsPanel(id='cont_tab', children=[contacts_page,], value="contacts_tab"),
            ],
        ),
    ],
)

right_pane = html.Div(
    id='right_pane',
    children=[right_tabs,],
)

