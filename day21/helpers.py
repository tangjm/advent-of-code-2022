import re
from schemas import Expression, Monkey, Constant

def parse_job(job): 
    arithmetic_expression = r'^(\w+)\s([\+|\-|\*|\/])\s(\w+)$' 
    match = re.match(arithmetic_expression, job)
    if match: 
        return Expression(match.group(2), Monkey(match.group(1)), Monkey(match.group(3)))
    else: 
        return Constant(int(job))