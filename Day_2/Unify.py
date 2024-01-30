def unify_variable(var,val, subsitution):
    if var in subsitution:
        return unify(subsitution[var], val, subsitution)
    elif val in subsitution:
        return unify(var, subsitution[val], subsitution)
    else:
        subsitution[var] = val
        return subsitution
    

def unify(term1,term2, subsitution=None):
    if subsitution is None:
        subsitution = {}

    if term1 == term2:
        return subsitution
    
    elif isinstance(term1, str) and term1.islower():
        return unify_variable(term1, term2, subsitution)
    
    elif isinstance(term2, str) and term2.islower():
        return unify_variable(term2, term1, subsitution)
    
    elif isinstance(term1, tuple) and isinstance(term2, tuple):
        if len(term1) != len(term2):
            return None
        for t1,t2 in zip(term1, term2):
            subsitution = unify(t1, t2, subsitution)
            if subsitution is None:
                return None
        return subsitution
    
    else:
        return None
    
# Example usage:

term1 = ('loves', 'John', 'X')
term2 = ('loves', 'John', 'Mary')

result_substitution = unify(term1, term2)

if result_substitution is not None:
    print("Unification sucessful")
    print(result_substitution)
else:
    print("Unification failed")

