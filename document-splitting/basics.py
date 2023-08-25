from langchain.text_splitter import RecursiveCharacterTextSplitter, CharacterTextSplitter

chunk_size = 26
chunk_overlap = 4

r_splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
c_splitter = CharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)

alphabet = 'abcdefghijklmnopqrstuvwxyz'
alphabet_with_more = 'abcdefghijklmnopqrstuvwxyzabcdefg'

print("recursive", r_splitter.split_text(alphabet))
print("recursive larger than chunk_size", r_splitter.split_text(alphabet_with_more))

spaced_alphabet = 'a b c d e f g h i j k l m n o p q r s t u v w x y z'

print("recursive", r_splitter.split_text(spaced_alphabet))

# by default, a CharacterTextSplitter will split on new lines
# but there are no new lines in this text
print("character", c_splitter.split_text(spaced_alphabet)) 

c_splitter_with_separator=CharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap, separator=' ')

print("character with separator", c_splitter_with_separator.split_text(spaced_alphabet))

