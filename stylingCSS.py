from nicegui import ui

ui.icon('thumb_up', color='#eb1010').classes('text-7xl')
ui.markdown('This is **Markdown**.')
ui.html('This is <strong>HTML</strong>.')
with ui.row():
    ui.label('Luna Alejandra').style('color: #058061; font-family:"Times New Roman", Georgia, serif; font-size: 24px' )
    ui.label('Tailwind').classes('font-serif')
    ui.label('Quasar').classes('q-ml-xl')
ui.link('NiceGUI on GitHub', 'https://github.com/zauberzeug/nicegui')

ui.run()