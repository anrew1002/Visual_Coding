def area(labeled,label=1):
    return (labeled[labeled == label] / label).sum()