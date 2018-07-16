#include <list>

class Solution {
public:
    bool isValid(string s) {
        if(s == "")
            return true;
        std::list<char> stack;
        
        for(std::string::iterator it = s.begin(); it != s.end(); ++it){
            switch(*it){
                case '(':
                    stack.push_front('(');
                    break;
                case '{':
                    stack.push_front('{');
                    break;
                case '[':
                    stack.push_front('[');
                    break;
                case ')':
                    if(stack.front() == '(')
                        stack.pop_front();
                    else
                        return false;
                    break;
                case '}':
                    if(stack.front() == '{')
                        stack.pop_front();
                    else
                        return false;
                    break;
                case ']':
                    if(stack.front() == '[')
                        stack.pop_front();
                    else
                        return false;
                    break;
            }
        }
    return stack.empty();
    }
};