        public static void createLog(string str, string filename)
        {
            StringBuilder sb = new StringBuilder();
            var time = DateTime.Now;
            string formattedTime = time.ToString("yyyy/MM/dd - hh:mm:ss");

            try
            {
                // Get the current directory.
                sb.Append(formattedTime + "\t" + str + "\n");
                //sb.Append(str + "\n");
                string path = Directory.GetCurrentDirectory();
                File.AppendAllText(path + filename + ".txt", sb.ToString());
                sb.Clear();

            }
            catch (Exception e)
            {
                Console.WriteLine("The process failed: {0}", e.ToString());
            }
        }
        
        #2022/03/09 - 08:55:08	Message
