using DelimitedFiles

function twomove(i::Int, j::Int, mat::Matrix)::Real
    if i*j==1
        return 0
    elseif i==1
        return mat[i, j-1]
    elseif j==1
        return mat[i-1, j]
    else
        return min(mat[i-1, j], mat[i, j-1])
    end
end

function fourmove(i::Int, j::Int, mat::Matrix, upbound::Real)::Real
    function value(i::Int, j::Int)::Real
        try 
            return mat[i,j]
        catch e
            return upbound
        end
    end
    return min(value(i-1, j),value(i, j-1),value(i+1, j),value(i, j+1))
end


function minpathsum(mat::Matrix)::Matrix
    m,n=size(mat)
    upbound=sum(mat)
    optbound=m*n

    cache=copy(mat)
    for i in 1:m
        for j in 1:n
            cache[i,j]+=twomove(i,j, cache)
        end
    end

    # iterative optimization to eliminate locality
    count=0
    while true
        flag=0
        for i in 1:m
            for j in 1:n
                altway=fourmove(i,j, cache, upbound)+mat[i,j]
                if altway<cache[i,j]
                    cache[i,j]=altway
                    flag+=1
                end
            end
        end
        count+=1
        if flag==0  
            println("optmization success")
            break
        elseif count>optbound
            println("bound hitted")
            break
        end
    end
    println("optimization count:", count)
    return cache
end

mat1=[131 673 234 103 18; 
201 96 342 965 150; 
630 803 746 422 111;
537 699 497 121 956;
805 732 524 37 331]

mat2=readdlm("p083_matrix.txt", ',')


cache=minpathsum(mat2)
println(cache[end,end])
