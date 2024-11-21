# import mistune
# from mistune import HTMLRenderer, Markdown
# from mistune.ast_renderer import ASTRenderer

# class MarkdownCleaner:
#     """Limpa o conteúdo Markdown removendo elementos irrelevantes."""

#     def __init__(self):
#         self.parser = Markdown(renderer=ASTRenderer())

#     def clean_markdown(self, markdown_text):
#         """Remove imagens, links de imagens e outros elementos irrelevantes."""
#         ast = self.parser(markdown_text)
#         cleaned_ast = self._clean_ast(ast)
#         cleaned_markdown = self._ast_to_markdown(cleaned_ast)
#         return cleaned_markdown

#     def _clean_ast(self, ast):
#         """Percorre e limpa a AST."""
#         if not isinstance(ast, list):
#             return ast

#         cleaned = []
#         for node in ast:
#             if node['type'] == 'image':
#                 # Ignora imagens
#                 continue
#             elif node['type'] == 'link' and node.get('children'):
#                 # Verifica se o link contém uma imagem
#                 if len(node['children']) == 1 and node['children'][0]['type'] == 'image':
#                     continue  # Ignora links que envolvem imagens
#                 else:
#                     # Limpa os filhos do link
#                     node['children'] = self._clean_ast(node['children'])
#                     cleaned.append(node)
#             elif node.get('children'):
#                 # Limpa os filhos recursivamente
#                 node['children'] = self._clean_ast(node['children'])
#                 cleaned.append(node)
#             else:
#                 cleaned.append(node)
#         return cleaned

#     def _ast_to_markdown(self, ast):
#         """Converte a AST limpa de volta para Markdown."""
#         renderer = CleanMarkdownRenderer()
#         return renderer.render(ast)


# class CleanMarkdownRenderer(HTMLRenderer):
#     """Renderer personalizado para converter AST de volta para Markdown."""

#     def render(self, ast):
#         self.result = ''
#         self._process(ast)
#         return self.result.strip()

#     def _process(self, ast):
#         for node in ast:
#             method = getattr(self, f"render_{node['type']}", None)
#             if method:
#                 method(node)
#             else:
#                 # Processa filhos se existirem
#                 if node.get('children'):
#                     self._process(node['children'])

#     def render_text(self, node):
#         self.result += node['text']

#     def render_paragraph(self, node):
#         self.result += '\n\n'
#         if node.get('children'):
#             self._process(node['children'])

#     def render_heading(self, node):
#         level = node['level']
#         self.result += '\n\n' + ('#' * level) + ' '
#         if node.get('children'):
#             self._process(node['children'])

#     def render_list(self, node):
#         for item in node['children']:
#             self.result += '\n\n- '
#             if item.get('children'):
#                 self._process(item['children'])

#     def render_block_quote(self, node):
#         self.result += '\n\n> '
#         if node.get('children'):
#             self._process(node['children'])

#     def render_emphasis(self, node):
#         self.result += '*'
#         if node.get('children'):
#             self._process(node['children'])
#         self.result += '*'

#     def render_strong(self, node):
#         self.result += '**'
#         if node.get('children'):
#             self._process(node['children'])
#         self.result += '**'

#     def render_code(self, node):
#         self.result += f"`{node['text']}`"

#     def render_thematic_break(self, node):
#         self.result += '\n\n---\n\n'

#     def render_line_break(self, node):
#         self.result += '  \n'

#     def render_link(self, node):
#         if node.get('children'):
#             self.result += '['
#             self._process(node['children'])
#             self.result += f']({node["link"]})'
#         else:
#             self.result += f'<{node["link"]}>'

