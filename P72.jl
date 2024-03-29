using Primes


function φ(n::Int)::Int
    factors=factor(Set,n)
    return n*prod([1-1//p for p in factors]) # totient number
end

function countfractons(n::Int)::Int
    primeslist=primes(n)
    count=0
    println("primes generated.")
    for i in 2:n
        if i in primeslist
            count+=i-1 # smaller than i
        else
            count+=φ(i)
        end
    end
    return count
end

countfractons(1000000)