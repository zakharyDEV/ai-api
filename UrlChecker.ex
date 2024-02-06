defmodule UrlChecker do  #The defmodule keyword is used to define a module named UrlChecker.
  def check_url(url, search_text) do #The check_url function takes a URL and a search text as parameters and uses
    case HTTPoison.get(url) do
      {:ok, %HTTPoison.Response{status_code: 200, body: body}} ->
        if String.contains?(body, search_text) do
          run_python_file()
          IO.puts("The text is present in the URL")
        else
          IO.puts("The text is not present in the URL")
        end
      {:error, reason} ->
        IO.puts("Error: Unable to reach the URL - #{reason}")
    end
  end

  defp run_python_file() do
    System.cmd("python", ["C:\Users\zakh\Music\AmichelPI\main.py"]) #change the path to your python file
  end
end

UrlChecker.check_url("http://michelai.org/api.html", "ApiKey=4BCi-QqbF-rzmg-CbeR-D") #change the url to your site and to the  api.html page
                                                                                      #and change the text to your actual api key
