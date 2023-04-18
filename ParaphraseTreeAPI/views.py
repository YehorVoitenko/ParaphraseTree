import random
from nltk.tree import Tree

from rest_framework.response import Response
from rest_framework.views import APIView


class Paraphrase(APIView):
    def get(self, request):
        # Required 'tree' url parameter
        tree = request.GET.get("tree")
        # Default 'limit' url parameter value
        limit = 20

        # Optional 'limit' url parameter
        if request.GET.get("limit"):
            limit = int(request.GET.get("limit"))

        result = []

        # Get from text Tree instance
        tree = Tree.fromstring(tree)

        for i in range(limit):
            # In result there are '\n' symbols, because of tree structure
            result.append({"tree": str(text_analyse(tree)).replace("\n  ", " ")})

        return Response({"paraphrases": result})


def text_analyse(main_tree: Tree) -> Tree:
    """
    Function gets tree structure and response processed tree, with shuffled NP (noun phrase).

    :param main_tree: Tree
    :return: main_tree: Tree
    """

    # If current object is Tree object - it splits to less chunk to find "NP" chunk
    if isinstance(main_tree, Tree):
        chunks = []
        if "NP" in str(main_tree).split()[0]:
            paraphrase_np_tree(main_tree)

        # This loop "reduce" chunks to minimum - to sting value
        # This way if value is string - it appends to main tree as value
        for chunk in main_tree:
            chunks.append(text_analyse(chunk))
        return Tree(main_tree.label(), chunks)

    # If current object is value(string), not Tree object - it just append to tree structure as value
    else:
        return main_tree


def paraphrase_np_tree(np_tree_chunk: Tree) -> Tree:
    """
    Function get NP chunks and shuffle inside chunks by random

    :param np_tree_chunk: Tree
    :return: np_tree_chunk: Tree
    """

    chunks = []
    # We receive "NP" chunk, so we need to see "inside NP" in this tree to get "inside NP" list
    for chunk in np_tree_chunk:

        # First argument in tree is part of speech abbreviation
        if "NP" in str(chunk).split()[0]:
            chunks.append(chunk)

    # Got inside NP and shuffle them to "paraphrase" it
    random.shuffle(chunks)

    # In finish, we need replace old chunks to new(shuffled)
    for i in range(len(np_tree_chunk)):
        if "NP" in str(np_tree_chunk[i]).split()[0]:
            # So we replace chunk (by index) received it the beginning Tree by last shuffled chunk
            np_tree_chunk[i] = chunks[-1]
            chunks.pop(-1)

    return np_tree_chunk
