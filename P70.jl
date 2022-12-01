using Primes

function φ(n::Int)::Int
    factors=factor(Set,n)
    return n*prod([1-1//p for p in factors]) # totient number
end

function ispermutation(a::Int, b::Int)
    a,b=string(a),string(b)
    if length(a)==length(b)
        return all([count(==(c), a)==count(==(c), b) for c in b])
    else
        return false
    end
end

function mintotient(n::Int)::Int
    j=0
    m=100000
    for i in 2:n
        if ispermutation(i,φ(i)) 
            r=i/φ(i)
            if r<m
                m=r
                j=i
            end
        end
    end
    return j
end

println(mintotient(10000000))

