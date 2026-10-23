"""Equal-share expense settlement with integer-paise arithmetic."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from common import Store, form, heading, note, table, run, money, rupees
store = Store(Path(__file__).with_name('data.json'), {'people': [], 'expenses': []})
def balances(people, expenses):
    result = {p: 0 for p in people}
    for expense in expenses:
        amount = expense['amount']
        members = expense['members']
        base, extra = divmod(amount, len(members))
        result[expense['payer']] += amount
        for index, member in enumerate(members):
            result[member] -= base + (1 if index < extra else 0)
    return result
def settle(result):
    debtors = [[p, -v] for p, v in result.items() if v < 0]
    creditors = [[p, v] for p, v in result.items() if v > 0]
    transfers, i, j = [], 0, 0
    while i < len(debtors) and j < len(creditors):
        amount = min(debtors[i][1], creditors[j][1])
        transfers.append([debtors[i][0], creditors[j][0], amount])
        debtors[i][1] -= amount
        creditors[j][1] -= amount
        if debtors[i][1] == 0:
            i += 1
        if creditors[j][1] == 0:
            j += 1
    return transfers
def view():
    out = note('Positive balance means receive money; negative means pay. Shares are equal among selected people.')
    out += form('people', [('people', 'Names separated by commas', 'text','Asha,Balu,Chitra')], 'Set participants')
    out += note('Participants: ' + ', '.join(store.data['people']))
    out += form('expense', [('description', 'Expense description', 'text', 'Taxi'),
    ('payer', 'Paid by exact participant name', 'text', ''),
    ('amount', 'Amount in rupees', 'text', '900.00'),
    ('members', 'Shared by names separated by commas', 'text',
    '')], 'Add expense')
    out += heading('Recorded expenses')
    out += table(['Description', 'Payer', 'Amount', 'Shared by'],
    [[e['description'], e['payer'], rupees(e['amount']), ','.join(e['members'])] for e in store.data['expenses']])
    result = balances(store.data['people'], store.data['expenses'])
    out += heading('Balances') + table(['Person', 'Net balance'], [(p, rupees(v)) for p,v in result.items()])
    out += heading('Suggested settlements')
    out += table(['Who pays', 'Who receives', 'Amount'], [(a, b, rupees(c)) for a, b, c in settle(result)])
    return out
def handle(data):
    if data['action'] == 'people':
        if store.data['expenses']:
            raise ValueError('Participants cannot be replaced after recording expenses.')
        people = [p.strip() for p in data['people'].split(',')]
        if len(people) < 2 or '' in people or len(set(people)) != len(people):
            raise ValueError('Use at least two unique nonempty names.')
        store.data['people'] = people
    elif data['action'] == 'expense':
        payer = data['payer'].strip()
        members = [p.strip() for p in data['members'].split(',')]
        people = store.data['people']
        amount = money(data['amount'])
        if payer not in people or not members or any(p not in people for p in members):
            raise ValueError('Payer and sharing names must be registered participants.')
        if len(set(members)) != len(members):
            raise ValueError('A sharing name appears twice.')
        description = data['description'].strip()
        if not description:
            raise ValueError('Enter a description.')
        store.data['expenses'].append({'description': description, 'payer': payer,
            'amount': amount, 'members': members})
    else:
         raise ValueError('Unknown action.')
    store.save()
if __name__ == '__main__':
    run('Shared Trip Expense Settler', view, handle)
