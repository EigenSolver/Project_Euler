using Primes

function φ(n::Int)::Int
    factors=factor(Set,n)
    return n*prod([1-1//p for p in factors]) # totient number
end

function countfractons(n::Int)::Int
    primeslist=primes(n)
    count=0
    println("primes generated.")
    for i in 4:n
        if i in primeslist
            count+=i-floor(Int,i/3)-ceil(Int,i/2) # smaller than i
        else
            factors=factor(Set,i)
            for j in ceil(Int,i/3):floor(Int, i/2)
                if all([j%f!=0 for f in factors])
                    count+=1
                end
            end
        end
    end
    return count
end

countfractons(12000)