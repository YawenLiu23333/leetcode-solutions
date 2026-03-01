class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        parts = []
        for part in path.split('/'):
            if part == '' or part == '.':
                continue
            if part == '..':
                if parts:
                    parts.pop()
            else:
                parts.append(part)

        return '/' + '/'.join(parts)


        