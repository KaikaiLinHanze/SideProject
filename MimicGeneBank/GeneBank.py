"""
File name: Genebank
Author:Kaikai Lin
Date:2021.11.26
Description:
This class is used to handle genebank file.
Furthermore it can get the definition, origin and feature.
"""
import re as re


def main():
    x = GenebankParser("CFTR_DNA.gb")
    x.read_file()
    print(x.get_feature_sequence())
    print(x.feature_list)
    print(x.feature_name)
    y = Feature(x.get_feature_sequence(), x.get_origin())

    y.separated_manipulation()


class Feature:
    """
    Just put anything you want in the Feature, I can output the data you need.
    Before get any data please choose the mode you want.
    """

    def __init__(self, get_sequence, get_origin):
        self.get_sequence = get_sequence
        self.get_origin = get_origin
        self.collect_sequence = []

    def collect_sequence(self):
        """
        This function is used to get sequence.
        :return: list, sequence
        """
        return self.collect_sequence

    def upper_cased_manipulate(self):
        pass

    def separated_manipulation(self):
        """
        To handle the sequence for join, complement, join combine complement and normal one.
        :return: collect the data of the sequence, it is separated version
        """
        for manipulate in self.get_sequence:
            if re.match(r"^[a-zA-Z]{6}", manipulate):
                if "join" not in manipulate:
                    #  complement
                    manipulate_string = manipulate[11:len(manipulate)-1].replace("..", " ").replace(">", " ").split()
                    first = int(manipulate_string[0]) - 1
                    second = int(manipulate_string[1])
                    output = self.get_origin[first: second]
                    output = output.replace("a", "1").replace("t", "2").replace("c", "3").replace("g", "4")
                    output = output.replace("1", "t").replace("2", "a").replace("3", "g").replace("4", "c")
                    self.collect_sequence.append(output)
                else:
                    # join & complement
                    manipulate_string = manipulate[16:len(manipulate)-2].replace("..", " ").replace(",", " ").split()
                    output = ""
                    for i in range(len(manipulate_string)):
                        if i % 2 == 0:
                            first = int(manipulate_string[i]) -1
                        else:
                            second = int(manipulate_string[i])
                            output += self.get_origin[first: second]
                    output = output.replace("a", "1").replace("t", "2").replace("c", "3").replace("g", "4")
                    output = output.replace("1", "t").replace("2", "a").replace("3", "g").replace("4", "c")
                    self.collect_sequence.append(output)
            elif re.match(r"^[a-zA-Z]{4}", manipulate):
                if "join" in manipulate:
                    manipulate_string = manipulate[5:len(manipulate)-1].replace("..", " ").replace(",", " ").split()
                    output = ""
                    for i in range(len(manipulate_string)):
                        if i % 2 == 0:
                            first = int(manipulate_string[i]) - 1
                        else:
                            second = int(manipulate_string[i])
                            output += self.get_origin[first: second]
                    self.collect_sequence.append(output)
                else:
                    manipulate_string = manipulate[6:len(manipulate)-1].replace(",", " ").split()
                    output = ""
                    for i in range(len(manipulate_string)):
                        if ".." in manipulate_string[i]:
                            first = manipulate_string[i].replace("..", " ").split()[0]
                            second = manipulate_string[i].replace("..", " ").split()[1]
                            output += self.get_origin[int(first)-1:int(second)]
                        else:
                            output += self.get_origin[int(manipulate_string[i])-1]
                    self.collect_sequence.append(output)
            else:
                if ".." in manipulate:
                    manipulate_string = manipulate.replace("..", " ").split()
                    output = ""
                    for i in range(len(manipulate_string)):
                        if i % 2 == 0:
                            first = int(manipulate_string[i]) - 1
                        else:
                            second = int(manipulate_string[i])
                            output += self.get_origin[first: second]
                    self.collect_sequence.append(output)
                else:
                    self.collect_sequence.append(self.get_origin[int(manipulate)-1])


class GenebankParser:
    """
    Before you process any data, you need to read the file.
    """

    def __init__(self, file):
        self.file = file
        self.definition = ""
        self.sequence = ""
        self.feature = ""
        self.feature_list = []
        self.feature_name = []
        self.feature_sequence = []
        self.origin = []

    def get_origin(self):
        """
        This function is used to get origin.
        Before get data please execute read the file.
        :return: str, origin
        """
        return "".join(self.origin).replace(" ", "")

    def get_definition(self):
        """
        This function is used to get definition.
        Before get data please execute read the file.
        :return:str, definition of the file
        """
        return self.definition

    def get_feature_list(self):
        """
        This function is used to get feature list.
        Before get data please execute read the file.
        :return: list, feature list
        """
        return self.feature_list

    def get_feature_sequence(self):
        """
        This function is used to get feature sequence.
        Before get data please execute read the file.
        :return: list, feature sequence
        """
        return self.feature_sequence

    def get_feature_name(self):
        """
        This function is used to get feature name.
        Before get data please execute read the file.
        :return: list, feature name.
        """
        return self.feature_name

    def read_file(self):
        """
        This function is used to collect the definition, feature data, and origin.
        :return: str, to make sure file is reading.
        """
        with open(self.file, mode="r") as r:
            all_file = r.read()
            whole_doc = "".join(all_file)
            self.definition = " ".join(re.search(r'(^DEFINITION)([^.]*)', whole_doc, re.MULTILINE).group(2).split())
            sequence = re.findall(r'(^[\s]{1,10}[\d]{1,7}[\s]{1})([\w\s]{1,65})', whole_doc, re.MULTILINE)
            feature = re.findall(r"(^\s{5}[a-zA-Z_]{1,13}[\s]{1,15})([^\/]*)([^\"]*)([\w\"\s]*)", whole_doc,
                                 re.MULTILINE)
            for feature_index in range(len(feature)):
                self.feature_list.append(feature[feature_index][0].strip())
                self.feature_sequence.append(feature[feature_index][1].strip().replace("\n                     ", ""))
                self.feature_name.append("".join(feature[feature_index][2:len(feature[feature_index])]).strip())
            for origin_index in range(len(sequence)):
                self.origin.append(sequence[origin_index][1])
        return f'File reading'


if __name__ == "__main__":
    main()