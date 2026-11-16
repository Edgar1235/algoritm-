import heapq
import math
import json
from collections import Counter


class Node:
    """Клас для представлення вузла дерева Хаффмана."""

    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    # Перевизначаємо оператор '<' для коректної роботи пріоритетної черги (heapq)
    def __lt__(self, other):
        return self.freq < other.freq


def build_huffman_tree(text):
    """Будує дерево Хаффмана на основі частот символів у тексті."""
    if not text:
        return None

    # 1. Підраховуємо частоту появи кожного символу
    frequencies = Counter(text)

    # Створюємо список вузлів (чергу з пріоритетами)
    heap = [Node(char, freq) for char, freq in frequencies.items()]
    heapq.heapify(heap)

    # Обробка виродженого випадку, коли в тексті лише 1 унікальний символ
    if len(heap) == 1:
        single_node = heapq.heappop(heap)
        root = Node(None, single_node.freq)
        root.left = single_node
        return root

    # 2-5. Об'єднуємо два вузли з найменшою вагою, поки не залишиться один корінь
    while len(heap) > 1:
        left_child = heapq.heappop(heap)
        right_child = heapq.heappop(heap)

        merged = Node(None, left_child.freq + right_child.freq)
        merged.left = left_child
        merged.right = right_child

        heapq.heappush(heap, merged)

    return heap[0]


def generate_codes(node, current_code="", codes=None):
    """Рекурсивно формує словник кодів шляхом обходу дерева від кореня до листків."""
    if codes is None:
        codes = {}
    if node is None:
        return codes

    # Якщо дійшли до листкового вузла — зберігаємо код символу
    if node.char is not None:
        codes[node.char] = current_code if current_code else "0"
        return codes

    generate_codes(node.left, current_code + "0", codes)
    generate_codes(node.right, current_code + "1", codes)
    return codes


def huffman_encode(text):
    """Кодує текстовий рядок за алгоритмом Хаффмана."""
    root = build_huffman_tree(text)
    codes = generate_codes(root)
    encoded_text = "".join(codes[char] for char in text)
    return encoded_text, codes, root


def huffman_decode(encoded_text, root):
    """Декодує бітовий рядок за допомогою дерева Хаффмана."""
    if not encoded_text or root is None:
        return ""

    decoded_chars = []
    current = root
    for bit in encoded_text:
        current = current.left if bit == "0" else current.right
        if current.char is not None:
            decoded_chars.append(current.char)
            current = root

    return "".join(decoded_chars)


def analyze_compression(text):
    """Виводить таблицю частот, коди та порівнює розмір з рівномірним кодом."""
    encoded_text, codes, root = huffman_encode(text)
    total_chars = len(text)
    unique_chars = len(codes)
    freqs = Counter(text)

    print(f"Вхідна фраза: «{text}»")
    print(f"Довжина фрази: {total_chars} символів | Унікальних символів: {unique_chars}\n")

    print(f"{'Символ':<10} | {'Частота':<10} | {'Вага (ймовірність)':<20} | {'Код Хаффмана'}")
    print("-" * 60)
    for char, freq in sorted(freqs.items(), key=lambda x: (-x[1], x[0])):
        weight = freq / total_chars
        display_char = repr(char) if char in (' ', '\n', '\t') else char
        print(f"{display_char:<10} | {freq:<10} | {weight:<20.2f} | {codes[char]}")

    # Розрахунок бітів для рівномірного кодування: ceil(log2(N)) біт на символ
    bits_per_symbol_uniform = math.ceil(math.log2(unique_chars)) if unique_chars > 1 else 1
    uniform_bits = total_chars * bits_per_symbol_uniform
    huffman_bits = len(encoded_text)

    print("\nЗакодований рядок:", encoded_text)
    print(f"Декодований рядок: «{huffman_decode(encoded_text, root)}»")
    print("-" * 60)
    print(f"Довжина кодом Хаффмана: {huffman_bits} біт")
    print(f"Довжина рівномірним кодом ({bits_per_symbol_uniform} біт/символ): {uniform_bits} біт")
    print(f"Економія пам'яті: {uniform_bits - huffman_bits} біт ({(1 - huffman_bits / uniform_bits) * 100:.1f}%)")


# =====================================================================
# ДОДАТКОВЕ ЗАВДАННЯ: АРХІВАТОР ТЕКСТОВИХ ФАЙЛІВ (СТИСНЕННЯ / РОЗПАКУВАННЯ)
# =====================================================================
def compress_file(input_filepath, output_filepath):
    """Стискає текстовий файл та зберігає бінарний архів із таблицею кодів."""
    with open(input_filepath, "r", encoding="utf-8") as f:
        text = f.read()

    if not text:
        print("Файл порожній.")
        return

    encoded_text, codes, _ = huffman_encode(text)

    # Доповнюємо бітовий рядок нулями до кратності 8 для пакування в байти
    padding = (8 - len(encoded_text) % 8) % 8
    padded_encoded_text = encoded_text + "0" * padding

    # Перетворюємо рядок бітів у масив байтів
    byte_array = bytearray()
    for i in range(0, len(padded_encoded_text), 8):
        byte = padded_encoded_text[i:i + 8]
        byte_array.append(int(byte, 2))

    # Зберігаємо службовий заголовок (словник кодів + кількість доданих нулів) і байти
    header = json.dumps({"padding": padding, "codes": codes}, ensure_ascii=False).encode("utf-8")
    header_length = len(header).to_bytes(4, byteorder="big")

    with open(output_filepath, "wb") as f:
        f.write(header_length)
        f.write(header)
        f.write(bytes(byte_array))

    print(f"\n[Архіватор] Файл '{input_filepath}' успішно стиснуто у '{output_filepath}'.")


def decompress_file(archive_filepath, output_filepath):
    """Розпаковує бінарний архів Хаффмана назад у текстовий файл."""
    with open(archive_filepath, "rb") as f:
        header_length = int.from_bytes(f.read(4), byteorder="big")
        header_data = json.loads(f.read(header_length).decode("utf-8"))
        compressed_bytes = f.read()

    padding = header_data["padding"]
    codes = header_data["codes"]
    reverse_codes = {v: k for k, v in codes.items()}

    # Відновлюємо бітовий рядок із байтів та відкидаємо доповнені нулі
    bit_string = "".join(f"{byte:08b}" for byte in compressed_bytes)
    if padding > 0:
        bit_string = bit_string[:-padding]

    # Декодуємо символи за зворотним словником
    decoded_chars = []
    current_code = ""
    for bit in bit_string:
        current_code += bit
        if current_code in reverse_codes:
            decoded_chars.append(reverse_codes[current_code])
            current_code = ""

    with open(output_filepath, "w", encoding="utf-8") as f:
        f.write("".join(decoded_chars))

    print(f"[Архіватор] Архів '{archive_filepath}' успішно розпаковано у '{output_filepath}'.")


# =====================================================================
# ДЕМОНСТРАЦІЯ РОБОТИ
# =====================================================================
if __name__ == "__main__":
    print("=== 1. ТЕСТ НА ФРАЗІ З МЕТОДИЧКИ ===")
    analyze_compression("абабагаламага")

    print("\n=== 2. ТЕСТ НА ДОВІЛЬНІЙ ФРАЗІ ===")
    analyze_compression("алгоритми та структури даних")

    print("\n=== 3. ПЕРЕВІРКА РОБОТИ АРХІВАТОРА ===")
    sample_file = "input.txt"
    archive_file = "compressed.huff"
    restored_file = "restored.txt"

    with open(sample_file, "w", encoding="utf-8") as f:
        f.write("Кодування Хаффмана — ефективний метод стиснення даних без втрат!\n" * 10)

    compress_file(sample_file, archive_file)
    decompress_file(archive_file, restored_file)