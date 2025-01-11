def test_arg(*argv):
    results = []
    for arg in argv:
        
        val= results.append(arg * 2)
        print("another arg", val)
    return results
test_arg(1,2,3,4,5,6,7)
