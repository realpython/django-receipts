from django.http import JsonResponse
from receipts.models import Receipt

def receipt_json(request):
    results = {
        "receipts":[],
    }

    for receipt in Receipt.objects.all():
        line = [str(receipt), []]
        for item in receipt.item_set.all():
            line[1].append(str(item))

        results["receipts"].append(line)

    return JsonResponse(results)
