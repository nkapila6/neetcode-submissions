class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
       st = []
       operands = ["+", "-", "*", "/"]

       for tok in tokens:
            if tok in operands:
                b, a = int(st.pop()), int(st.pop())

                if tok == "+":
                    st.append(a+b)

                if tok == "-":
                    st.append(a-b)

                if tok == "*":
                    st.append(a*b)

                if tok == "/":
                    st.append(a/b)

            else:
                st.append(tok)


       return int(st.pop())