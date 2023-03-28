import re


def solution(new_id):
    new_id = new_id.lower()
    new_id = re.sub('[^a-z0-9-_.]', '', new_id)
    new_id = re.sub('\\.{2,}', '.', new_id)
    new_id = new_id.strip('.') if len(new_id) > 1 else new_id.replace('.', '')
    new_id = 'a' if not new_id else new_id
    new_id = new_id[:15]
    new_id = new_id.strip('.') if len(new_id) > 1 else new_id.replace('.', '')
    new_id = new_id + new_id[-1] * (3 - len(new_id)) if len(new_id) <= 2 else new_id

    return new_id

new_id = "...!@BaT#*..y.abcdefghijklm"
print(solution(new_id))
