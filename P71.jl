
function main()
    target=3/7
    delta::Float64=0.0
    flag::Float64=1.0
    record=(0,0)
    for d in 10:1000000
        n::Int=floor(target*d)
        delta=target-n/d
        if delta>0
            if delta<flag
                flag=delta
                record=(n,d)
            else
                continue
            end
        elseif delta==0
            continue
        else
            break
        end
    end
    println(record)
end

main()