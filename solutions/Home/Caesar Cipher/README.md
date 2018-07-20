Your mission is to encrypt a secret message (text only, without special chars like "!", "&", "?" etc.) using Caesar cipher where each letter of input text is replaced by another that stands at a fixed distance. For example ("a b c", 3) == "d e f"

Input: A secret message as a string (lowercase letters only and white spaces)
Output: The same string, but encrypted

Precondition:
0 < len(text) < 50
-26 < delta < 26