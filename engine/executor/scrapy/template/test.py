# -*- coding: utf-8 -*-

import os
import re
import logging
from string import Template

logger = logging.getLogger()


def generate_file(path, name='', **kwargs):
    with open(path, 'rb') as fp:
        raw = ''
        while fp:
            line = fp.readline()
            reg = re.search('^\[(?P<block_name>[a-zA-Z]*.*)\]$', line)
            if reg:
                re_name = reg.group('block_name')
                if name == re_name:
                    logger.info('find name')
                else:
                    raw += line

    content = Template(raw).substitute(**kwargs)

    render_path = path[:-len('.tmpl')] if path.endswith('.tmpl') else path
    with open(render_path, 'wb') as fp:
        fp.write(content.encode('utf8'))
    if path.endswith('.tmpl'):
        os.remove(path)


if __name__ == "__main__":
    generate_file('./parse.tmpl',
                  function_id='function_one',
                  request_method='get')
