from collections    import OrderedDict 


maxdmg_name         = 'maxdmg'
maxdmg_description  = 'Set of tools for generation of text document generators'
maxdmg_github       = 'github_link'
maxdmg_demo         = 'demo_link'
maxdmg_tech         = ['Flask', 'Dash', 'Redis', 'Postgres', 'sqlalchemy', 'Docker',] 

projects = OrderedDict({
    'maxdmg' : {
        'name'  : maxdmg_name,
        'desc'  : maxdmg_description,
        'link'  : maxdmg_github,
        'demo'  : maxdmg_demo,
        'tech'  : maxdmg_tech,
    },
}) 

tools = OrderedDict([
    ('languages', ['c', 'c++', 'python', 'html', 'css', 'sql']),
    ('frameworks', ['flask', 'dash', 'sqlalchemy',]),
    ('databases', ['postgres', 'sqlite', 'redis',]),
    ('system', ['linux', 'nginx', 'docker',]),
])

commands = OrderedDict([
    ('help',    "Get this handy menu."),
    ('whois',   "Figure out who is the website owner."),
    ('projects',"Look at projects of the website owner."),
    ('contacts',"View contacts of the website owner."),
    ('banner',  "Display the header."),
    ('clear',   "Clear the terminal."),
])

contacts = OrderedDict([
    ('email',   'contact@tonotonokon.com'),
])

banner = [ 
    "  __      __       __                 ",
    " / /____ / /____  / /_____    ___  ___",
    "/ __/ _ / __/ _ \/  '_/ _ \  / _ \(_-<",
    "\__/_//_\__/_//_/_/\_/_//_/  \___/___/",
] 

prompt = 'guest@tonotonokon:~$'

