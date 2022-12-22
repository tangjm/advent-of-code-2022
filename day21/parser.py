import re
from schemas import Expression, Monkey, Constant

def parse_job(job): 
    arithmetic_expression = r'^(\w+)\s([\+|\-|\*|\/])\s(\w+)$' 
    match = re.match(arithmetic_expression, job)
    if match: 
        return Expression(match.group(2), Monkey(match.group(1)), Monkey(match.group(3)))
    else: 
        return Constant(int(job))

def parse_file(filename):
    with open(filename, 'rt') as f:
        lines = f.read().rstrip().split('\n')
        split = list(map(lambda x:x.split(': '), lines))

        monkeys = [ monkey for monkey, job in split ]
        jobs = [ job for monkey, job in split ]

        parsed_jobs = list(map(parse_job, jobs))

        zipped = list(zip(monkeys, parsed_jobs))

        # Map monkey names to Expressions/Constants 
        monkey_to_job = dict(zipped) 
    return monkey_to_job
