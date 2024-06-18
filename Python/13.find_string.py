def count_substring(string, substring):
        count=0
            st=0
                while st<=len(string):
                            st=string.find(substring,st)
                                    if st!=-1:
                                                    count+=1
                                                                st+=1
                                                                        else: break
                                                                                
                                                                                    return count

                                                                                if __name__ == '__main__':
                                                                                        string = input().strip()
                                                                                            sub_string = input().strip()
                                                                                                
                                                                                                    count = count_substring(string, sub_string)
                                                                                                        print(count)
