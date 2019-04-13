using Primes

# GG


function count_fractons(boundary::Int,report=false)
    primes_list=primes(boundary)
    println("primes generated..")
    count=0
    progress=0
    for n in 2:boundary
        if report
            if mod(n,boundary÷10)==0
                progress+=10
                println("progress: ",progress,"%")
            end
        end
        if n in primes_list
            count+=n-1
        else
            count+=1
            for p in primes_list
                if p<n && mod(n,p)=0
                    
                end
            end
        end
    end
    print(count)
end

count_fractons(8)
# count_fractons(1000000,true)