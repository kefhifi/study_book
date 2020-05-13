# 10. 文件和异常
# 10.1 文件操作
with open('pi_digits.txt',encoding='utf-8') as file_object:
    contents = file_object.read()
    print(contents)
# 在这个程序中，第1行代码做了大量的工作。我们先来看看函数open()。要以任何方式使用文件——哪怕仅仅是打印其内容，都得先打开文件，这样才能访问它。
# 函数open()接受一个参数：要打开的文件的名称。Python在当前执行的文件所在的目录中查找指定的文件。在这个示例中，当前运行的是file_reader.py，
# 因此Python在file_reader.py所在的目录中查找pi_digits.txt。函数open()返回一个表示文件的对象。
# 在这里，open('pi_digits.txt')返回一个表示文件pi_digits.txt的对象；Python将这个对象存储在我们将在后面使用的变量中。
# 关键字with在不再需要访问文件后将其关闭。在这个程序中，注意到我们调用了open()，但没有调用close()；
# 你也可以调用open()和close()来打开和关闭文件，但这样做时，如果程序存在bug，导致close()语句未执行，文件将不会关闭。
# 这看似微不足道，但未妥善地关闭文件可能会导致数据丢失或受损。如果在程序中过早地调用close()，你会发现需要使用文件时它已关闭（无法访问），
# 这会导致更多的错误。并非在任何情况下都能轻松确定关闭文件的恰当时机，但通过使用前面所示的结构，可让Python去确定：你只管打开文件，
# 并在不需要使用它时，Python自会在合适的时候自动将其关闭。

# 10.1.3 逐行读取
filename = 'pi_digits.txt'
with open(filename,encoding='utf-8') as file_object:
    for line in file_object:
        print(line,end="")

# 10.1.4 创建一个包含文件各行内容的列表
# 使用关键字with时，open()返回的文件对象只在with代码块内可用。如果要在with代码块外访问文件的内容，
# 可在with代码块内将文件的各行存储在一个列表中，并在with代码块外使用该列表：你可以立即处理文件的各个部分，也可推迟到程序后面再处理。
filename = 'pi_digits.txt'
with open(filename) as file_object:
    lines = file_object.readlines()
for line in lines:
    print(line.rstrip())
# 方法readlines()从文件中读取每一行，并将其存储在一个列表中；接下来，该列表被存储到变量lines中；在with代码块外，
# 我们依然可以使用这个变量。在❷处，我们使用一个简单的for循环来打印lines中的各行。
# 由于列表lines的每个元素都对应于文件中的一行，因此输出与文件内容完全一致。

# 10.1.5 使用文件的内容


# 10.1.6 包含一百万位的大型文件









