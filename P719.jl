using ProgressMeter

function assemble(digs::Vector{<:Int})::Int
    return reduce((x, y) -> 10x + y, reverse(digs))
end

function splitttingnumber(n::Int, digs::Vector{<:Int}=[])::Bool
    if n<0
        return false
    elseif n==0
        if digs==[]
            return true
        else
            return false
        end
    else
        k=assemble(digs)
        if k<n 
            return false
        elseif k == n 
            return true
        else
            l=length(digs)
            return [splitttingnumber(n-assemble(digs[1:i]), digs[i+1:l]) for i in 1:l]|>any
        end
    end
end


splitttingnumber(N::Int)::Bool=splitttingnumber(N, digits(N^2))

S=0
@showprogress for i in 2:10^6
    if splitttingnumber(i)
        global S+=i^2
    end
end
