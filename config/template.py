# Theme layout templates directory

# Template config
# ? Easily change the template configuration from here
# ? Replace this object with template-config/demo-*.py file's TEMPLATE_CONFIG to change the template configuration as per our demos
TEMPLATE_CONFIG = {
    "layout": "horizontal",             # Options[String]: vertical(default), horizontal
    "theme": "theme-default",         # Options[String]: theme-default(default), theme-bordered, theme-semi-dark
    "style": "light",                 # Options[String]: light(default), dark, system mode
    "rtl_support": True,              # options[Boolean]: True(default), False # To provide RTLSupport or not
    "rtl_mode": False,                # options[Boolean]: False(default), True # To set layout to RTL layout  (myRTLSupport must be True for rtl mode)
    "has_customizer": True,           # options[Boolean]: True(default), False # Display customizer or not THIS WILL REMOVE INCLUDED JS FILE. SO LOCAL STORAGE WON'T WORK
    "display_customizer": True,       # options[Boolean]: True(default), False # Display customizer UI or not, THIS WON'T REMOVE INCLUDED JS FILE. SO LOCAL STORAGE WILL WORK
    "content_layout": "wide",      # options[String]: 'compact', 'wide' (compact=container-xxl, wide=container-fluid)
    "navbar_type": "fixed",           # options[String]: 'fixed', 'static', 'hidden' (Only for vertical Layout)
    "header_type": "fixed",           # options[String]: 'static', 'fixed' (for horizontal layout only)
    "menu_fixed": True,               # options[Boolean]: True(default), False # Layout(menu) Fixed (Only for vertical Layout)
    "menu_collapsed": False,          # options[Boolean]: False(default), True # Show menu collapsed, Only for vertical Layout
    "footer_fixed": False,            # options[Boolean]: False(default), True # Footer Fixed
    "show_dropdown_onhover": True,    # True, False (for horizontal layout only)
    "customizer_controls": [
        "rtl",
        "style",
        "headerType",
        "contentLayout",
        "layoutCollapsed",
        "showDropdownOnHover",
        "layoutNavbarOptions",
        "themes",
    ],  # To show/hide customizer options
}

# Theme Variables
# ? Personalize template by changing theme variables (For ex: Name, URL Version etc...)
THEME_VARIABLES = {
    "creator_name": "ThemeSelection",
    "creator_url": "https://webagencia.com.br/",
    "template_name": "Jobs",
    "template_suffix": "",
    "template_version": "2.0.0",
    "template_free": False,
    "template_description": "Mural de vagas e oportunidades do Senai",
    "template_keyword": "vagas, empregos, senai",
    "facebook_url": "",
    "twitter_url": "",
    "github_url": "",
    "dribbble_url": "",
    "instagram_url": "",
    "license_url": "",
    "live_preview": "",
    "product_page": "https://themeselection.com/item/materio-bootstrap-django-admin-template/",
    "support": "https://themeselection.com/support/",
    "more_themes": "https://themeselection.com/",
    "documentation": "https://demos.themeselection.com/materio-bootstrap-html-admin-template/documentation",
    "changelog": "",
    "git_repository": "https://github.com/themeselection/materio-bootstrap-html-django-admin-template",
    "git_repo_access": "https://tools.themeselection.com/github/github-access",
}

# ! Don't change THEME_LAYOUT_DIR unless it's required
THEME_LAYOUT_DIR = "layout"
