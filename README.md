# balance_brackets
to balance brackets in a string be removing unmatched chars

Examples
 
balance("()") -> "()"
balance("a(b)c)") -> "a(b)c"
balance(")(") -> ""
balance("(((((") -> ""
balance("(()()(") -> "()()"
balance(")(())(") -> "(())"
balance(")())(()()(") -> "()()()" 

There can be multiple correct results per input:
balance("(())())") -> "(()())" or "(())()"
