  data = sub.readall.Data;
    x = zeros(size(data,1));
    y = zeros(size(data,1));
    z = zeros(size(data,1));
    for i= 1:size(data, 1)
        chardata = char(data(i, :));
        x(i) = str2double(chardata(1:7));
        y(i) = str2double(chardata(9:16));
        z(i) = str2double(chardata(18:25));
    end
    plot3(x, y, z, 'o')