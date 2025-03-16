def filter_anagrams_linked_lists(word_list):
    """
    Filters a list of words, returning only anagrams, and returns a sorted linked list.

    Args:
        word_list: A list of strings (words).

    Returns:
        A sorted linked list of anagrams.
    """

    anagram_groups = {}  # Dictionary to store anagram groups, key: sorted signature, value: sorted linked list
    for word in word_list:
        signature = "".join(sorted(word))  # Create a sorted signature of the word
        if signature in anagram_groups:
            anagram_groups[signature] = sorted_insert(anagram_groups[signature], word)  # Insert into existing group
        else:
            anagram_groups[signature] = {"value": word, "next": None}  # Create new group

    # Extract linked lists that have more than one element (anagrams)
    anagrams_lists = [group for group in anagram_groups.values() if group["next"] is not None]

    if not anagrams_lists:  # If no anagram groups are found
        return None

    merged_list = merge_sorted_linked_lists(anagrams_lists)  # Merge the sorted linked lists
    return merged_list

def sorted_insert(head, word):
    """Inserts a word into a sorted linked list."""
    new_node = {"value": word, "next": None}
    if head is None or word < head["value"]:  # Insert at the beginning
        new_node["next"] = head
        return new_node
    current = head
    while current["next"] and current["next"]["value"] < word:  # Find the correct position
        current = current["next"]
    new_node["next"] = current["next"]  # Insert the new node
    current["next"] = new_node
    return head

def merge_sorted_linked_lists(lists):
    """Merges a list of sorted linked lists into a single sorted linked list."""
    if not lists:
        return None
    if len(lists) == 1:
        return lists[0]

    merged = lists[0]  # Initialize with the first list
    for i in range(1, len(lists)):  # Merge remaining lists one by one
        merged = merge_two_lists(merged, lists[i])
    return merged

def merge_two_lists(list1, list2):
    """Merges two sorted linked lists."""
    if not list1:
        return list2
    if not list2:
        return list1

    if list1["value"] < list2["value"]:  # Choose the head of the merged list
        head = list1
        list1 = list1["next"]
    else:
        head = list2
        list2 = list2["next"]
    current = head

    while list1 and list2:  # Merge until one list is exhausted
        if list1["value"] < list2["value"]:
            current["next"] = list1
            list1 = list1["next"]
        else:
            current["next"] = list2
            list2 = list2["next"]
        current = current["next"]

    if list1:  # Append remaining nodes
        current["next"] = list1
    elif list2:
        current["next"] = list2

    return head

# Example usage
word_list = ["pool","loco","cool","stain","satin","pretty","nice", "dne","goog","traart","end","loop"]
result = filter_anagrams_linked_lists(word_list)

# Print the linked list
if result:
    current = result
    while current:
        print(current["value"])
        current = current["next"]