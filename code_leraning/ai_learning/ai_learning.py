from langchain_community.llms import tongyi
from langchain.prompts import PromptTemplate
from langchain.output_parsers import StructuredOutputParser, ResponseSchema
from settings import BAILIAN_API_KEY


llm = tongyi.Tongyi(api_key=BAILIAN_API_KEY)

# 提示词模板
prompt_template = "你是一个{role}, 请用{style}风格回答问题:{question}"
prompt_template_doctor = PromptTemplate.from_template(prompt_template)

# 输出格式化
response_schemas = [
    ResponseSchema(name='name', description='人的姓名', type='string'),
    ResponseSchema(name='age', description='人的年龄', type='int')
]
output_parser = StructuredOutputParser.from_response_schemas(response_schemas)
output_format_template = '''你是一个信息提取帮手，请从下文提取出姓名与年龄, 以JSON形式返回:
文本：{input_text}
{format_instructions}'''
output_format_prompt = PromptTemplate(
    template=output_format_template,
    partial_variables={"format_instructions": output_parser.get_format_instructions()}
)


if __name__ == '__main__':
    # 提示词模板使用方法
    # filled_prompt = prompt_template_doctor.format(role='资深医生', style='通俗易懂并尽可能简洁', question='什么是癌症')
    # info = llm.invoke(filled_prompt)
    # print(info)
    # 输出格式化使用方法
    input_text = "今天遇到了37岁的老板张三，他是上海人"
    filled_prompt = output_format_prompt.format(input_text=input_text)
    info = llm.invoke(filled_prompt)
    parsed_output = output_parser.parse(info)
    print(parsed_output)