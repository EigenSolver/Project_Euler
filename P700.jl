function eulercoin(n::Int)::Int128
    x=convert(Int128,1504170715041707)
    y=convert(Int128,4503599627370517)
    return mod(x*n,y) 
end

eulerarr=[eulercoin(n) for n in 1:100000000]


flag=eulerarr[1]
s=flag
for e in eulerarr
    global flag
    global s
    if e < flag
        s+=e
        flag=e
        println(e)
    end 
end

println(s)

