from dash           import (
    html, 
    dcc,
    Patch,
)
import dash_mantine_components as dmc
import uuid 
from .static        import ( 
    commands,
    projects,
    contacts,
    banner,
    prompt,
)


def GetPatch(inp: str):
    patch = Patch()
    raw_out = __ProcessInput(inp)
    if not raw_out:
        patch.clear()
        return patch

    term_label_text = html.Span(
        children=[prompt],
        className='font prompt_col',
    )

    l = term_label_text
    i = html.Span( 
        children=[str(inp),],
        className='prompt_inp',
    )
    t = html.Div([l,i])

    patch.extend([t,raw_out])
    return patch

def GetBanner():
    return __GetBanner()

def __ProcessInput(inp: str) -> str:
    clean = __ClearInput(inp)
    match clean:
        case 'help':
            return __GetHelp()
        case 'whois':
            return __GetWhois()
        case 'projects':
            return __GetProjects()
        case 'contacts':
            return __GetContacts()
        case 'banner':
            return __GetBanner()
        case 'clear':
            return None
        case 'test':
            return __GetTest()
        case _:
            return __GetWrongCommand()

def __ClearInput(inp: str) -> str:
    return inp.strip().lower()

def __GetHelp():
    e = __GetCommandElem()
    e.children=[
        html.Div([
            html.Div([
                html.Div([k], className='command',), 
                html.Div([v], className='command_desc',)
            ]) for k, v in commands.items()
        ])
    ]
    return e

def __GetWhois():
    e = __GetCommandElem()
    e.children=[
        html.Div([
            html.Div(["Hi, I'm Anton!"]),
            html.Div([html.Span(['Long story short'], className='term_out_emp_1'),", I was a lawyer, but one day the dog ate my tie. All of them..."]),
        ]),
            html.Div(["So I was left no choise but to join an amazing field of software development and solve real world problems with my products."]),
    ]
    return e

def __GetProjects():
    e = __GetCommandElem()
    e.children=[
        html.Div([
            html.Div([
                html.Div([
                    html.Span(["Name: "], className='project_title'), 
                    html.Span([v['name']]),
                ]),
                html.Div([
                    html.Span(["Desc: "], className='project_title'),
                    html.Span([v['desc']]),
                ]),
                html.Div([
                    html.Span(["Link: "], className='project_title'),
                    html.Span([v['link']]),
                ]),
                html.Div([
                    html.Span(["Demo: "], className='project_title'),
                    html.Span([v['demo']]),
                ]),
                html.Div([
                    html.Span(["Tech: "], className='project_title'),
                    html.Span([', '.join(v['tech'])]),
                ]),
            ]) for k, v in projects.items()
        ]),
    ]
    return e

def __GetContacts():
    e = __GetCommandElem()
    e.children=[
        html.Div([
            html.Div([
                html.Span(["email - "], className='project_title'), 
                html.A([contacts['email']],href=contacts['email']),
            ])
        ]),
    ]
    return e

def __GetBanner():
    e = __GetCommandElem()
    e.children=[
        html.Div([
            html.Div([
                html.Div([
                    html.Div([
                        html.Div([b]),
                    ]) for b in banner
                ], className='banner_pic')
            ]),
            html.Div([
                'Welcome to my interactive terminal!'
            ], className='banner_text',),
            html.Div([
                'Type ', html.Span(['help'], className='command'), ' to see a list of available commands.',
            ], className='banner_text',),
        ], className='banner')
    ]
    return e

def __GetTest():
    e = __GetCommandElem()
    e.children=['Wow, you found my SECRET ', html.Span(['test'], className='command'), ' command!',]
    return e

def __GetWrongCommand():
    e = __GetCommandElem()
    e.children=[ 'It seems like the terminal does not support this command. For list of availale commands type ', html.Span(['help'], className='command'),'.',
    ]
    return e

def __GetCommandElem():
    return html.P(
        className='typing-animation command_output', key=str(uuid.uuid4()),
    )



