from pygments.lexer import RegexLexer
from pygments.lexer import RegexLexer, bygroups, default, words, include
from pygments.token import Comment, Error, Keyword, Name, Number, \
    Punctuation, Operator, String, Text, Whitespace
import re

class ZiYue4DLexer(RegexLexer):
    name = 'ZiYue4D'
    aliases = ['ziyue4d']
    filenames = ['*.sb']

    bb_sktypes = r'@{1,2}|[#$%@]'
    bb_name = r'[a-z]\w*'
    bb_var = (rf'({bb_name})(?:([ \t]*)({bb_sktypes})|([ \t]*)([.])([ \t]*)(?:({bb_name})))?')

    flags = re.MULTILINE | re.IGNORECASE
    tokens = {
        'root': [
            # Text
            (r'\s+', Whitespace),
            # Comments
            (r";.*?\n", Comment.Single),
            (r"/(?:\\\n)?[*](?:[^*]|[*](?!(?:\\\n)?/))*[*](?:\\\n)?/", Comment.MultiLine),
            # Data types
            ('"', String.Double, 'string'),
            # Numbers
            (r'[0-9]+\.[0-9]*(?!\.)', Number.Float),
            (r'\.[0-9]+(?!\.)', Number.Float),
            (r'[0-9]+', Number.Integer),
            (r'\$[0-9a-f]+', Number.Hex),
            (r'\%[10]+', Number.Bin),
            # Other
            (words(('Shl', 'Shr', 'Sar', 'Mod', 'Or', 'And', 'Not',
                    'Abs', 'Sgn', 'Handle', 'Int', 'Float', 'Str',
                    'First', 'Last', 'Before', 'After'),
                   prefix=r'\b', suffix=r'\b'),
             Operator),
            (r'([&+\-*/~=<>^])', Operator),
            (r'[(),:\[\]\\]', Punctuation),
            (rf'\.([ \t]*)({bb_name})', Name.Label),
            # Identifiers
            (rf'\b(New)\b([ \t]+)({bb_name})',
             bygroups(Keyword.Reserved, Whitespace, Name.Class)),
            (rf'\b(Gosub|Goto)\b([ \t]+)({bb_name})',
             bygroups(Keyword.Reserved, Whitespace, Name.Label)),
            (rf'\b(Object)\b([ \t]*)([.])([ \t]*)({bb_name})\b',
             bygroups(Operator, Whitespace, Punctuation, Whitespace, Name.Class)),
            (rf'\b{bb_var}\b([ \t]*)(\()',
             bygroups(Name.Function, Whitespace, Keyword.Type, Whitespace, Punctuation,
                      Whitespace, Name.Class, Whitespace, Punctuation)),
            (rf'\b(Function)\b([ \t]+){bb_var}',
             bygroups(Keyword.Reserved, Whitespace, Name.Function, Whitespace, Keyword.Type,
                      Whitespace, Punctuation, Whitespace, Name.Class)),
            (rf'\b(Type)([ \t]+)({bb_name})',
             bygroups(Keyword.Reserved, Whitespace, Name.Class)),
            # Keywords
            (r'\b(Pi|True|False|Null)\b', Keyword.Constant),
            (r'\b(Local|Global|Const|Field|Dim)\b', Keyword.Declaration),
            (words((
                'End', 'Return', 'Exit', 'Chr', 'Len', 'Asc', 'New', 'Delete', 'Insert',
                'Include', 'Function', 'Type', 'If', 'Then', 'Else', 'ElseIf', 'EndIf',
                'For', 'To', 'Next', 'Step', 'Each', 'While', 'Wend',
                'Repeat', 'Until', 'Forever', 'Select', 'Case', 'Default',
                'Goto', 'Gosub', 'Data', 'Read', 'Restore', 'Extern'), prefix=r'\b', suffix=r'\b'),
             Keyword.Reserved),
            # Final resolve (for variable names and such)
            # (r'(%s)' % (bb_name), Name.Variable),
            (bb_var, bygroups(Name.Variable, Whitespace, Keyword.Type,
                              Whitespace, Punctuation, Whitespace, Name.Class)),
        ],
        'string': [
            (r'""', String.Double),
            (r'"C?', String.Double, '#pop'),
            (r'\\([\\abfnrtv"\']|x[a-fA-F0-9]{2,4}|'
             r'u[a-fA-F0-9]{4}|U[a-fA-F0-9]{8}|[0-7]{1,3})', String.Escape),
            (r'[^"\n]+', String.Double),
        ],
    }
