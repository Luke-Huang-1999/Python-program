# Hash 特性：
# 同一個物件在其生命週期內，Hash 值必須保持一致。

print(f"hash('cat') = {hash('cat')}")
print(f"hash(3.89) = {hash(3.89)}")
# print(f"hash('[79,12]') = {hash([79,12])}") # List 是可變動（Mutable）的物件，不可雜湊
print(f"hash((12, 45)) = {hash((12, 45))}")
print(f"hash(198) = {hash(198)}")
# print(f"hash({36 ,66}) = {hash({36 ,66})}")  # Set 是可變動（Mutable）的物件，不可雜湊
print(f"hash((98, )) = {hash((98, ))}")
# print(f"hash(['Python']) = {hash(['Python'])}") # List 是可變動（Mutable）的物件，不可雜湊
# print(f"hash((0.81,[4] )) = {hash((0.81,[4] ))}")# List 是可變動（Mutable）的物件，不可雜湊
# print(f"hash({'P':12}) = {hash({'P':12})}")# dict 是可變動（Mutable）的物件，不可雜湊
