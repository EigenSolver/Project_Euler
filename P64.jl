function continuedfraction(x::Real)::Tuple{Int, Real}
    i=floor(Int, x)
    r=1/(x-i) #remain
    return i, r
end


# function squareroots(N::Int, lim::Int=10)::Vector
#     n0,x0=continuedfraction(sqrt(big(N)))
#     expansion=zeros(Int,lim)
#     expansion[1]=n0
#     x=copy(x0)
#     for i in 2:lim
#         n,x=continuedfraction(x)
#         expansion[i]=n
#         if abs(x-x0)<1e-5
#             break
#         end
#     end
#     return expansion
# end

# function periodcount(expansion::Vector{<:Real})::Int
#     return sum([i!=0 for i in expansion])-1
# end

function periodcount(N::Int,lim::Int=10000)::Int
    n0,x0=continuedfraction(sqrt(big(N)))
    @assert x0 isa BigFloat
    x=copy(x0)
    count=0
    for i in 1:lim
        n,x=continuedfraction(x)
        count+=1
        if abs(x-x0)<1e-3
            break
        end
        if i==lim
            println(N)
        end
    end
    return count
end

function nonsquared(N::Int)
    n=floor(Int, sqrt(N))
    mask=ones(Bool,N)
    for i in 1:n
        mask[i^2]=false
    end
    return collect(1:N)[mask]
end


N=10000
lim=500

list=nonsquared(N)
M=length(list)
periods=zeros(Int,M)
for i in 1:M
    periods[i]=periodcount(list[i])
end

println(periods)