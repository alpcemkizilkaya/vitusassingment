class FindDiffIds:
    """
    Find Difference Between List of Ids
    """

    def find_diff(self, list_of_ids, diff_limit = 1):
        """
        Find difference between element of list according to diff limit
        :param list_of_ids: List of ids
        :type list_of_ids: list
        :param diff_limit: Char difference limit between ids
        :type diff_limit : int
        :return: List of ids separated by '-' which are filtered by diff limit
        :rtype: list
        """
        result = []
        for i in range(len(list_of_ids)):
            for j in range(len(list_of_ids)):
                diffs = 0
                # j which are smaller than i are already checked
                if j > i:
                    for k in range(len(list_of_ids[i])):
                        if list_of_ids[i][k] != list_of_ids[j][k]:
                            diffs = diffs + 1
                if diffs == diff_limit:
                    result.append(list_of_ids[i]+"-"+list_of_ids[j])
        return result