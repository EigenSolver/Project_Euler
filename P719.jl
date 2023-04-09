function is_S_number(k::Int)
    n=k^2
    s=map(x->parse(Int,x),split(string(n),""))|>sum
    return s
end

N=100

for k in 1:N
    n=k^2
