import sys
print(sys.argv)

if len(sys.argv) == 1:
    sys.argv.append('runserver')

print(sys.argv)
