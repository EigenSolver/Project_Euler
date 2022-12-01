using Combinatorics

N=16
gon=5
digits=1:10

# N=9
# gon=3
# digits=1:6
function main(N::Int,gon::Int,digits::Vector{Int})::Int128

    sets=combinations(digits, 3)

    legalsets=[]
    for s in sets
        if sum(s) == N
            push!(legalsets, s)
        end
    end

    println("number of 16-sum wings:", length(legalsets))

    pentagonsets=[]

    for p in combinations(legalsets, gon)
        flatten = vcat(p...)
        if all([i in flatten for i in digits])
            legal=true
            ninternal=0
            nexternal=0
            for i in digits
                count=sum([i in wing for wing in p])
                if count==1
                    nexternal+=1
                elseif count==2
                    ninternal+=1
                else
                    legal=false
                    break
                end
            end
            if ninternal==nexternal==gon
            else
                legal=false 
            end
            if legal
                push!(pentagonsets,p)
            end
        end
    end

    println("number of possible pentagon sets:", length(pentagonsets))



    function swap(i::Int, j::Int, vec::Vector)
        vec[i],vec[j]=vec[j],vec[i]
    end

    function representation(magicgon::Vector{Vector{Int}})
        n=length(magicgon)
        # determine external and 
        internal=[]
        external=[]
        for i in digits
            if sum([i in wing for wing in magicgon])==2
                push!(internal,i)
            else
                push!(external,i)
            end
        end

        # find start wing
        rep=[]
        w1=zeros(3)
        p1=minimum(external)
        for w in magicgon
            if p1 in w
                for i in 1:3
                    if w[i]==p1
                        swap(i,1,w)
                    end
                end
                w1=w
                
                break
            end
        end

        if w1[2]<w1[3]
            swap(2,3,w1)
        end

        push!(rep, w1)
        plast=w1[2]
        pnext=w1[3]
        count=0
        while length(rep)<n+1
            for w in magicgon
                w=copy(w)
                if !(plast in w) && pnext in w
                    for i in 1:3
                        if w[i]==pnext
                            swap(i,2,w)
                            break
                        end
                    end # exchange order of middle
                    if w[1] in internal
                        swap(1,3,w)
                    end
                    push!(rep, w)
                    plast=w[2]
                    pnext=w[3]
                    break
                end
            end
            count+=1
            if count>2n
                return 0#collect(repeat(zeros(Int8,3),gon))
            end
        end
        if rep[end]!=rep[1]
            return 0#collect(repeat(zeros(Int8,3),gon))
        end

        magicgon=rep[1:gon]
        str=vcat(magicgon...)|>join
        if length(str)>16
            return 0
        else
            return parse(Int128, str)
        end
    end

    if pentagonsets!=[]
        reps=map(representation, pentagonsets)
        return maximum(reps)
    else
        return 0
    end
end


results=[]
for N in 12:20
    push!(results,main(N,5,collect(1:10)))
end

println(maximum(results))