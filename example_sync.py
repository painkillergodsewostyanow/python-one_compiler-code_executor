from code_executor import CodeExecutor

code_executor = CodeExecutor(
    "token:str",
    'lang_id:str'
)

result = code_executor.execute('print(input(), input()', 'hellow\nworld')

print(result)
