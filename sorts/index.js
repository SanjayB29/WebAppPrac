function showCode() {
    const algorithm = document.getElementById("sorting-algorithm").value;
    const codeContainer = document.getElementById("code-container");
    const code = getSortingCode(algorithm);
    codeContainer.textContent = code;
}

function getSortingCode(algorithm) {
    switch (algorithm) {
        case "bubble-sort":
            return `def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]`;

        case "selection-sort":
            return `def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]`;

        case "insertion-sort":
            return `def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key`;

        case "quick-sort":
            return `def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less = [x for x in arr[1:] if x <= pivot]
        greater = [x for x in arr[1:] if x > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)`;

        case "merge-sort":
            return `def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1`;

        case "counting-sort":
            return `def counting_sort(arr):
    max_val = max(arr)
    min_val = min(arr)
    range_of_elements = max_val - min_val + 1

    count_arr = [0] * range_of_elements
    output_arr = [0] * len(arr)

    for i in range(len(arr)):
        count_arr[arr[i] - min_val] += 1

    for i in range(1, len(count_arr)):
        count_arr[i] += count_arr[i - 1]

    for i in range(len(arr) - 1, -1, -1):
        output_arr[count_arr[arr[i] - min_val] - 1] = arr[i]
        count_arr[arr[i] - min_val] -= 1

    for i in range(len(arr)):
        arr[i] = output_arr[i]`;

        case "radix-sort":
            return `def counting_sort_radix(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10

    for i in range(n):
        index = (arr[i] // exp)
        count[index % 10] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    i = n - 1
    while i >= 0:
        index = (arr[i] // exp)
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1

    for i in range(n):
        arr[i] = output[i]

def radix_sort(arr):
    max_val = max(arr)
    exp = 1

    while max_val // exp > 0:
        counting_sort_radix(arr, exp)
        exp *= 10`;

        case "bucket-sort":
            return `def bucket_sort(arr):
    max_val = max(arr)
    min_val = min(arr)
    range_of_elements = max_val - min_val + 1
    bucket_size = range_of_elements // len(arr)

    buckets = [[] for _ in range(len(arr))]

    for num in arr:
        index = (num - min_val) // bucket_size
        buckets[index].append(num)

    for i in range(len(arr)):
        insertion_sort(buckets[i])

    k = 0
    for i in range(len(arr)):
        for j in range(len(buckets[i])):
            arr[k] = buckets[i][j]
            k += 1`;

        default:
            return "Select an algorithm from the dropdown.";
    }
}

function copyToClipboard() {
    const codeContainer = document.getElementById("code-container");
    const codeText = codeContainer.textContent;
    const textArea = document.createElement("textarea");
    textArea.value = codeText;
    document.body.appendChild(textArea);
    textArea.select();
    document.execCommand("copy");
    document.body.removeChild(textArea);
    alert("Code copied to clipboard!");
}
