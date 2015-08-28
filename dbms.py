import sqlparse


class Dbms:

    def __init__(self):
        self.__query = []
        self.__input = ''
        pass

    def __error_message__(self, code):
        error_msg_dict = {
            0 : "Thanks for using skbly7's DBMS. Bye.",
            1064 : "ERROR 1064 (42000): You have an error in your SQL syntax; "
                   "check the manual for the right syntax to use."
        }
        return error_msg_dict[code]

    def __break_n_execute_query__(self):
        for query in self.__query:
            self.__execute__(query)

    def __type_verify_wrapper__(self, parsed_query):
        type = parsed_query.get_type()
        verified = True
        if type == u'UNKNOWN':
            if str.upper(str(parsed_query.tokens[0])) == u'EXIT':
                print self.__error_message__(0)
                exit(0)
            else:
                print self.__error_message__(1064)
                verified = False
        return verified

    def __execute__(self, query):
        parsed_query = sqlparse.parse(query)[0]
        type_verified = self.__type_verify_wrapper__(parsed_query)
        if type_verified:
            print 'Execute query : ', query

    def execute(self, input):
        self.__input = input
        self.__query = sqlparse.split(self.__input)
        self.__break_n_execute_query__()