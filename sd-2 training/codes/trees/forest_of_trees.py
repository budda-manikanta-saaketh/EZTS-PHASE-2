#dictionary (forest of 3 trees):
families={'charley':{'sam':{'boxy','rosy'},'niia':{'pepsi'}},'devi':{'tommy':{'tony'},'timmy':{'hamster'},'tammy':{'hamster'}},'carlos':{'diego':'cat','ferret':'fox'}}
for parent, children in families.items():
    print(f"{parent} has {len(children)} kid(s):")
    print(f"{' and '.join([str(child) for child in [*children]])}")